import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import numpy as np
import pyreadstat
import os
from scipy.stats import chi2

class DataCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Odkurzacz Danych - Kontrola Jakości (QC) V3")
        self.root.geometry("850x900")
        self.spss_path = ""
        self.variables = []
        
        # Słowniki przechowujące stany checkboxów dla poszczególnych filtrów
        self.straight_chk = {}
        self.long_chk = {}
        self.mah_chk = {}
        
        self.create_widgets()

    def create_checklist(self, parent):
        """Tworzy przewijany panel z checkboxami"""
        container = tk.Frame(parent)
        container.pack(fill=tk.X, pady=5)
        canvas = tk.Canvas(container, height=120, bg="white", highlightthickness=1, highlightbackground="#ccc")
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.X, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        return scrollable_frame

    def create_widgets(self):
        # GŁÓWNY SCROLLBAR OKNA
        self.main_canvas = tk.Canvas(self.root)
        self.main_scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.main_canvas.yview)
        self.scrollable_main = ttk.Frame(self.main_canvas)
        self.scrollable_main.bind("<Configure>", lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))
        self.main_canvas.create_window((0, 0), window=self.scrollable_main, anchor="nw")
        self.main_canvas.configure(yscrollcommand=self.main_scrollbar.set)
        self.main_canvas.pack(side="left", fill="both", expand=True)
        self.main_scrollbar.pack(side="right", fill="y")

        frame = self.scrollable_main

        # 1. Wczytanie pliku
        frame_top = tk.Frame(frame)
        frame_top.pack(fill=tk.X, pady=10, padx=20)
        tk.Button(frame_top, text="1. Wczytaj bazę SPSS", bg="#ff9800", fg="white", font=('Arial', 10, 'bold'), command=self.load_spss).pack(side=tk.LEFT)
        self.lbl_file = tk.Label(frame_top, text="Brak pliku", fg="gray")
        self.lbl_file.pack(side=tk.LEFT, padx=10)

        # 2. Speederzy
        f_speed = tk.LabelFrame(frame, text="Filtr 1: Speederzy (Zbyt szybkie wypełnienie)", font=('Arial', 10, 'bold'), padx=10, pady=10)
        f_speed.pack(fill=tk.X, padx=20, pady=5)
        self.chk_speed = tk.BooleanVar(value=True)
        tk.Checkbutton(f_speed, text="Aktywuj filtr", variable=self.chk_speed).pack(anchor=tk.W)
        tk.Label(f_speed, text="Zmienna mierząca czas:").pack(anchor=tk.W)
        self.combo_time = ttk.Combobox(f_speed, state="readonly", width=40)
        self.combo_time.pack(anchor=tk.W)
        tk.Label(f_speed, text="Próg odrzucenia (w % mediany czasu):").pack(anchor=tk.W)
        self.entry_speed_thr = tk.Entry(f_speed, width=10)
        self.entry_speed_thr.insert(0, "30")
        self.entry_speed_thr.pack(anchor=tk.W)

        # 3. Straightlinerzy (Z CHECKBOXAMI)
        f_straight = tk.LabelFrame(frame, text="Filtr 2: Straightlinerzy (Brak wariancji w baterii)", font=('Arial', 10, 'bold'), padx=10, pady=10)
        f_straight.pack(fill=tk.X, padx=20, pady=5)
        self.chk_straight = tk.BooleanVar(value=True)
        tk.Checkbutton(f_straight, text="Aktywuj filtr", variable=self.chk_straight).pack(anchor=tk.W)
        tk.Label(f_straight, text="Zaznacz pytania matrycowe:").pack(anchor=tk.W)
        self.frame_straight_vars = self.create_checklist(f_straight)

        # 4. Long Strings (Z CHECKBOXAMI)
        f_long = tk.LabelFrame(frame, text="Filtr 3: Long Strings (Identyczne odpowiedzi pod rząd)", font=('Arial', 10, 'bold'), padx=10, pady=10)
        f_long.pack(fill=tk.X, padx=20, pady=5)
        self.chk_long = tk.BooleanVar(value=True)
        tk.Checkbutton(f_long, text="Aktywuj filtr", variable=self.chk_long).pack(anchor=tk.W)
        tk.Label(f_long, text="Zaznacz pytania matrycowe:").pack(anchor=tk.W)
        self.frame_long_vars = self.create_checklist(f_long)
        tk.Label(f_long, text="Maksymalna dozwolona długość ciągu (np. 5):").pack(anchor=tk.W)
        self.entry_long_thr = tk.Entry(f_long, width=10)
        self.entry_long_thr.insert(0, "5")
        self.entry_long_thr.pack(anchor=tk.W)

        # 5. Braki Danych
        f_miss = tk.LabelFrame(frame, text="Filtr 4: Braki danych (Missing Values)", font=('Arial', 10, 'bold'), padx=10, pady=10)
        f_miss.pack(fill=tk.X, padx=20, pady=5)
        self.chk_miss = tk.BooleanVar(value=True)
        tk.Checkbutton(f_miss, text="Aktywuj filtr", variable=self.chk_miss).pack(anchor=tk.W)
        tk.Label(f_miss, text="Maksymalny % dozwolonych braków w ankiecie (np. 50):").pack(anchor=tk.W)
        self.entry_miss_thr = tk.Entry(f_miss, width=10)
        self.entry_miss_thr.insert(0, "50")
        self.entry_miss_thr.pack(anchor=tk.W)

        # 6. Mahalanobis (Z CHECKBOXAMI)
        f_mah = tk.LabelFrame(frame, text="Filtr 5: Odległość Mahalanobisa (Multivariate Outliers)", font=('Arial', 10, 'bold'), padx=10, pady=10)
        f_mah.pack(fill=tk.X, padx=20, pady=5)
        self.chk_mah = tk.BooleanVar(value=True)
        tk.Checkbutton(f_mah, text="Aktywuj filtr", variable=self.chk_mah).pack(anchor=tk.W)
        tk.Label(f_mah, text="Zaznacz zmienne numeryczne do modelu:").pack(anchor=tk.W)
        self.frame_mah_vars = self.create_checklist(f_mah)
        tk.Label(f_mah, text="Próg p-value dla odrzucenia (np. 0.001):").pack(anchor=tk.W)
        self.entry_mah_thr = tk.Entry(f_mah, width=10)
        self.entry_mah_thr.insert(0, "0.001")
        self.entry_mah_thr.pack(anchor=tk.W)

        # 7. Przycisk
        tk.Button(frame, text="URUCHOM CZYSZCZENIE I ZAPISZ", bg="#4CAF50", fg="white", font=('Arial', 12, 'bold'), command=self.clean_data).pack(pady=20)

    def load_spss(self):
        path = filedialog.askopenfilename(filetypes=[("SPSS Files", "*.sav")])
        if path:
            self.spss_path = path
            self.lbl_file.config(text=os.path.basename(path))
            df, meta = pyreadstat.read_sav(path)
            self.variables = meta.column_names
            self.combo_time['values'] = self.variables
            
            # Czyszczenie starych checkboxów
            for frame in [self.frame_straight_vars, self.frame_long_vars, self.frame_mah_vars]:
                for widget in frame.winfo_children(): widget.destroy()
            
            self.straight_chk.clear()
            self.long_chk.clear()
            self.mah_chk.clear()
            
            # Generowanie nowych checkboxów
            for var in self.variables:
                v_str, v_lng, v_mah = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()
                
                tk.Checkbutton(self.frame_straight_vars, text=var, variable=v_str, bg="white").pack(anchor=tk.W)
                tk.Checkbutton(self.frame_long_vars, text=var, variable=v_lng, bg="white").pack(anchor=tk.W)
                tk.Checkbutton(self.frame_mah_vars, text=var, variable=v_mah, bg="white").pack(anchor=tk.W)
                
                self.straight_chk[var] = v_str
                self.long_chk[var] = v_lng
                self.mah_chk[var] = v_mah

    def get_max_consecutive(self, row):
        vals = row.dropna().values
        if len(vals) == 0: return 0
        max_len, current_len = 1, 1
        for i in range(1, len(vals)):
            if vals[i] == vals[i-1]:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1
        return max_len

    def clean_data(self):
        if not self.spss_path:
            messagebox.showwarning("Błąd", "Wczytaj bazę!")
            return
            
        df, meta = pyreadstat.read_sav(self.spss_path)
        initial_len = len(df)
        df['DO_USUNIECIA'] = 0
        raport = []

        if self.chk_speed.get() and self.combo_time.get():
            var = self.combo_time.get()
            thr = float(self.entry_speed_thr.get()) / 100
            limit = df[var].median() * thr
            df['FLAGA_SPEEDER'] = np.where(df[var] < limit, 1, 0)
            df.loc[df['FLAGA_SPEEDER'] == 1, 'DO_USUNIECIA'] = 1
            raport.append(f"Speederzy: {df['FLAGA_SPEEDER'].sum()}")

        vars_straight = [var for var, state in self.straight_chk.items() if state.get()]
        if self.chk_straight.get() and len(vars_straight) > 1:
            df['FLAGA_STRAIGHT'] = np.where(df[vars_straight].std(axis=1) == 0, 1, 0)
            df.loc[df['FLAGA_STRAIGHT'] == 1, 'DO_USUNIECIA'] = 1
            raport.append(f"Straightlinerzy: {df['FLAGA_STRAIGHT'].sum()}")

        vars_long = [var for var, state in self.long_chk.items() if state.get()]
        if self.chk_long.get() and len(vars_long) > 1:
            thr = int(self.entry_long_thr.get())
            df['MAX_STRING'] = df[vars_long].apply(self.get_max_consecutive, axis=1)
            df['FLAGA_LONGSTR'] = np.where(df['MAX_STRING'] >= thr, 1, 0)
            df.loc[df['FLAGA_LONGSTR'] == 1, 'DO_USUNIECIA'] = 1
            raport.append(f"Long Strings: {df['FLAGA_LONGSTR'].sum()}")

        if self.chk_miss.get():
            thr = float(self.entry_miss_thr.get()) / 100
            pct_missing = df.isnull().sum(axis=1) / len(df.columns)
            df['FLAGA_BRAKI'] = np.where(pct_missing > thr, 1, 0)
            df.loc[df['FLAGA_BRAKI'] == 1, 'DO_USUNIECIA'] = 1
            raport.append(f"Duże braki danych: {df['FLAGA_BRAKI'].sum()}")

        vars_mah = [var for var, state in self.mah_chk.items() if state.get()]
        if self.chk_mah.get() and len(vars_mah) > 1:
            df_sub = df[vars_mah].dropna()
            if not df_sub.empty:
                cov = np.cov(df_sub.values.T)
                inv_cov = np.linalg.pinv(cov)
                mean = np.mean(df_sub.values, axis=0)
                diff = df_sub.values - mean
                md = np.diag(diff.dot(inv_cov).dot(diff.T))
                
                p_values = 1 - chi2.cdf(md, len(vars_mah))
                thr_p = float(self.entry_mah_thr.get())
                
                df['FLAGA_MAHALANOBIS'] = 0
                outlier_indices = df_sub.index[p_values < thr_p]
                df.loc[outlier_indices, 'FLAGA_MAHALANOBIS'] = 1
                df.loc[df['FLAGA_MAHALANOBIS'] == 1, 'DO_USUNIECIA'] = 1
                raport.append(f"Mahalanobis Outliers: {len(outlier_indices)}")

        df_clean = df[df['DO_USUNIECIA'] == 0].copy()
        cols_to_drop = [c for c in df_clean.columns if c.startswith('FLAGA_') or c in ['DO_USUNIECIA', 'MAX_STRING']]
        df_clean.drop(columns=cols_to_drop, inplace=True, errors='ignore')

        save_dir = r"C:\DP_Bazy"
        os.makedirs(save_dir, exist_ok=True)
        out_path = os.path.join(save_dir, f"Oczyszczone_{os.path.basename(self.spss_path)}")
        
        clean_meta_cols = [c for c in meta.column_names if c in df_clean.columns]
        clean_meta_labs = [meta.column_labels[meta.column_names.index(c)] for c in clean_meta_cols]
        pyreadstat.write_sav(df_clean, out_path, column_labels=clean_meta_labs, variable_value_labels=meta.variable_value_labels)
        
        raport_str = "\n".join(raport)
        messagebox.showinfo("Raport z Czyszczenia", f"Baza początkowa: {initial_len}\n\nWYKRYTO:\n{raport_str}\n\nOdrzucono ogółem: {initial_len - len(df_clean)}\nBaza końcowa: {len(df_clean)}\n\nZapisano w: {out_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataCleanerApp(root)
    root.mainloop()