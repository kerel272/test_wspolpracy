#!/usr/bin/env python3

import sys
import argparse
import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city, country="", units='metric'):
    location = f"{city},{country}" if country else city
    try:
        response = requests.get(f"https://wttr.in/{location}?format=j1", timeout=10)
        response.raise_for_status()
        data = response.json()
        current = data['current_condition'][0]
        temp_c = float(current['temp_C'])
        wind_kmh = float(current['windspeedKmph'])

        if units == 'imperial':
            temp = temp_c * 9/5 + 32  # °F
            wind = wind_kmh * 0.621371  # mph
        else:
            temp = temp_c  # °C
            wind = wind_kmh / 3.6  # przelicz km/h na m/s

        return temp, wind
    except Exception as e:
        raise ValueError(f"Nie udało się pobrać pogody dla '{location}'. Sprawdź nazwę lub połączenie.")

def show_gui():
    def on_submit():
        city = entry_city.get().strip()
        country = entry_country.get().strip()
        unit = 'imperial' if var_units.get() == 'imperial' else 'metric'
        if not city:
            messagebox.showwarning("Błąd", "Wprowadź miasto!")
            return
        try:
            temp, wind = get_weather(city, country, unit)
            unit_temp = "°F" if unit == 'imperial' else "°C"
            unit_wind = "mph" if unit == 'imperial' else "m/s"
            result_label.config(text=f"Temperatura: {temp:.1f}{unit_temp}\nWiatr: {wind:.1f} {unit_wind}")
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    root = tk.Tk()
    root.title("Pogoda (bez klucza!)")
    root.geometry("320x220")

    tk.Label(root, text="Miasto:").pack(pady=5)
    entry_city = tk.Entry(root)
    entry_city.pack()

    tk.Label(root, text="Kraj (np. PL, US):").pack(pady=5)
    entry_country = tk.Entry(root)
    entry_country.pack()

    var_units = tk.StringVar(value='metric')
    tk.Radiobutton(root, text="Europejskie (°C, m/s)", variable=var_units, value='metric').pack()
    tk.Radiobutton(root, text="Amerykańskie (°F, mph)", variable=var_units, value='imperial').pack()

    tk.Button(root, text="Pokaż pogodę", command=on_submit).pack(pady=10)
    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.pack()
    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Pogoda bez klucza API (via wttr.in)")
    parser.add_argument("--city", help="Nazwa miasta")
    parser.add_argument("--country", default="", help="Kod kraju (np. PL, US)")
    parser.add_argument("--units", choices=["metric", "imperial"], default="metric")
    parser.add_argument("--gui", action="store_true", help="Uruchom GUI")

    args = parser.parse_args()

    if args.gui:
        show_gui()
    elif args.city:
        try:
            temp, wind = get_weather(args.city, args.country, args.units)
            unit_temp = "°F" if args.units == 'imperial' else "°C"
            unit_wind = "mph" if args.units == 'imperial' else "m/s"
            print(f"Temperatura: {temp:.1f}{unit_temp}")
            print(f"Prędkość wiatru: {wind:.1f} {unit_wind}")
        except Exception as e:
            print("Błąd:", e, file=sys.stderr)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
