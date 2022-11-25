standard_defects = ["NaN", "", " ", 0 ]

head_rows = 10 # Number of rows that pands.DataFrame.head shows for preview

uniqueness_tracker = 1000
remove_blanks_tracker = 1000

sys_path = "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code"

to_gramm = {"KG": 1000, "Kg": 1000, "kg": 1000, "T": 1_000_000, "t": 1000_000_000}
to_kg = {"G": 0.001, "g": 0.001, "T": 1000, "t": 1000}
to_ton = {"KG": 0.001, "Kg": 0.001, "kg": 0.001, "T": 0.000001, "t": 0.000001}

to_m = {"dm": 0.1, "Dm": 0.1, "DM": 0.1, "mm": 0.001, "Mm": 0.001, "MM": 0.001, "cm": 0.01, "Cm": 0.01, "CM": 0.01}
to_mm = {"dm": 100, "Dm": 100, "DM": 100, "m": 1000, "M": 1000, "cm": 10, "Cm": 10, "CM": 10}
to_cm = {"dm": 10, "Dm": 10, "DM": 10, "m": 100, "M": 100, "mm": 0.1, "Mm": 0.1, "MM": 0.1}
to_dm = {"cm": 0.1, "Cm": 0.1, "CM": 0.1, "m": 10, "M": 10, "mm": 0.01, "Mm": 0.01, "MM": 0.01}

sizes_XXS_XXL = ["XXS", "S", "M", "L", "XL", "XXL"]
sizes_XS_XL = ["XS", "S", "M", "L", "XL"]

data_quality_dimensions = ["relevancy", "free_of_error", "completeness", "redundancy"]