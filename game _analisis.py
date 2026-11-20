import pandas as pd
import matplotlib.pyplot as plt

# Video Game Sales Analysis Project

data = {
    "Game": [
        "GTA V", "Minecraft", "FIFA 23", "PUBG",
        "Call of Duty", "Mario Kart", "Fortnite",
        "Red Dead Redemption", "The Sims 4", "Valorant"
    ],
    "Genre": [
        "Action", "Adventure", "Sports", "Action",
        "Action", "Racing", "Action", "Adventure",
        "Simulation", "Action"
    ],
    "Platform": [
        "PC", "PC", "PlayStation", "Mobile",
        "PC", "Nintendo", "PC", "PlayStation",
        "PC", "PC"
    ],
    "Sales": [185, 150, 90, 75, 80, 60, 95, 55, 40, 35]
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv("gaming_data.csv", index=False)

# Display data
print("\nVIDEO GAME SALES DATA")
print(df)

# Total sales
print("\nTotal Sales:", df["Sales"].sum(), "Million")

# Best selling game
best = df.loc[df["Sales"].idxmax()]
print("\nBest Selling Game:", best["Game"])

# Genre analysis
genre = df.groupby("Genre")["Sales"].sum()
print("\nGenre Sales:")
print(genre)

# Platform analysis
platform = df.groupby("Platform")["Sales"].sum()
print("\nPlatform Sales:")
print(platform)

# Graph 1
df.sort_values("Sales").plot(
    x="Game", y="Sales", kind="bar",
    title="Video Game Sales Analysis",
    legend=False
)
plt.ylabel("Sales (Million)")
plt.tight_layout()
plt.savefig("game_sales.png")
plt.show()

# Graph 2
genre.plot(kind="bar", title="Sales by Genre")
plt.ylabel("Sales (Million)")
plt.tight_layout()
plt.savefig("genre_analysis.png")
plt.show()

# Graph 3
platform.plot(kind="pie", autopct="%1.1f%%",
              title="Platform Sales")
plt.ylabel("")
plt.tight_layout()
plt.savefig("platform_analysis.png")
plt.show()

print("\nPROJECT COMPLETED SUCCESSFULLY!")