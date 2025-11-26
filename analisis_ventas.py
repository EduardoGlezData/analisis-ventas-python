import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventas.csv")
df["fecha"] = pd.to_datetime(df["fecha"])
df["ingreso"] = df["cantidad"] * df["precio_unitario"]

print("\nPrimeras filas:")
print(df.head())

df["mes"] = df["fecha"].dt.to_period("M").astype(str)
ventas_mes = df.groupby("mes")["ingreso"].sum().reset_index()
print("\nVentas por mes:")
print(ventas_mes)

ventas_producto = df.groupby("producto")["ingreso"].sum().reset_index()
print("\nIngresos por producto:")
print(ventas_producto)

top = ventas_producto.sort_values("ingreso", ascending=False).iloc[0]
print("\nProducto más rentable:")
print(top)

plt.figure()
plt.plot(ventas_mes["mes"], ventas_mes["ingreso"], marker="o")
plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Ingresos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.bar(ventas_producto["producto"], ventas_producto["ingreso"])
plt.title("Ingresos por producto")
plt.xlabel("Producto")
plt.ylabel("Ingresos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
