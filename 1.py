import pandas as pd
import matplotlib.pyplot as plt
brand_urls = {
    "ZARA": "https://www.zara.com",
    "H&M": "https://www.hm.com",
    "UNIQLO": "https://www.uniqlo.com",
    "GU": "https://www.gu-global.com"
}

# 讀資料
df = pd.read_csv("data.csv")

#加入CP值
df["cp"] = df["rating"] / df["price"]

#基本分析
print("平均價格（各品牌）")
print(df.groupby("brand")["price"].mean())

print("\n各類型平均價格")
print(df.groupby("type")["price"].mean())

print("\nCP值分析")
print(df[["brand", "type", "price", "rating", "cp"]])

#視覺化
plt.style.use("ggplot")  

#價格分布
plt.figure(figsize=(6,4))
plt.hist(df["price"], bins=5)
plt.title("Price Distribution", fontsize=14)
plt.xlabel("Price", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig("price_distribution.png")

#品牌平均價格
plt.figure(figsize=(6,4))
avg_price = df.groupby("brand")["price"].mean()
avg_price.plot(kind="bar")

plt.title("Average Price by Brand", fontsize=14)
plt.xlabel("Brand", fontsize=12)
plt.ylabel("Average Price", fontsize=12)

#在柱狀圖上顯示數字
for i, v in enumerate(avg_price):
    plt.text(i, v + 20, f"{v:.0f}", ha='center')

plt.tight_layout()
plt.savefig("brand_price.png")

#類型比例
plt.figure(figsize=(6,6))
df["type"].value_counts().plot(
    kind="pie",
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Type Distribution", fontsize=14)
plt.ylabel("") 
plt.tight_layout()
plt.savefig("type_distribution.png")

plt.show()
#推薦系統
budget = int(input("\n請輸入你的預算："))
cloth_type = input("請輸入類型（T-shirt / Dress / Jacket）：")

filtered = df[(df["price"] <= budget) & (df["type"] == cloth_type)]

if filtered.empty:
    print("找不到符合條件的商品")
else:
    #用CP值排序
    best = filtered.sort_values(by="cp", ascending=False).iloc[0]

    print("推薦結果：")
    print(f"品牌：{best['brand']}")
    print(f"類型：{best['type']}")
    print(f"價格：{best['price']}")
    print(f"評分：{best['rating']:.1f}")
    print(f"CP值：{best['cp']:.4f}")
    website = brand_urls.get(best["brand"], "無官方網站")
print(f"官方網站：{website}")