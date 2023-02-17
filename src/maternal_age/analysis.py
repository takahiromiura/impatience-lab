import pandas as pd


def main():
    # データを読み込む
    DATA_PATH = "data/raw/maternal_age.csv"
    df = pd.read_csv(DATA_PATH, skiprows=6, na_values="-", thousands=",")

    # データの前処理

    # 不要な列の削除
    df = df.drop(
        columns=[
            "表章項目",
            "性別",
            "/母の年齢(5歳階級)",
            "不詳",
        ]
    )

    # 列名の変更
    df = df.rename(
        columns={
            "時間軸(年次)": "year",
            "都道府県（特別区－指定都市再掲）": "prefecture",
            "総数": "num",
            "14歳以下": "age_below_14",
            "15～19歳": "age_between_15_19",
            "20～24歳": "age_between_20_24",
            "25～29歳": "age_between_25_29",
            "30～34歳": "age_between_30_34",
            "35～39歳": "age_between_35_39",
            "40～44歳": "age_between_40_44",
            "45～49歳": "age_between_45_49",
            "50歳以上": "age_over_50",
        }
    )

    # 欠損値の穴埋め
    df = df.fillna(value=0)

    # 年を整数型に変更する
    df.year = df.year.str.replace("年", "").astype(int)

    # 高齢出産数・率を計算する
    df["normal_birth"] = df[
        [
            "age_between_20_24",
            "age_between_25_29",
            "age_between_30_34",
        ]
    ].sum(axis=1)

    df["late_birth"] = df[
        [
            "age_between_35_39",
            "age_between_40_44",
            "age_between_45_49",
            "age_over_50",
        ]
    ].sum(axis=1)

    df["late_birth_rate"] = df["late_birth"] / (
        df["normal_birth"] + df["late_birth"]
    )

    # データ分析

    # 記述統計
    summary = df["late_birth_rate"].describe()
    print(summary)

    # 年別平均
    mean_by_year = df.groupby("year")["late_birth_rate"].mean()
    print(mean_by_year)

    # 都道府県ランク
    mean_by_prefecture = df.groupby("prefecture")[["late_birth_rate"]].mean()
    mean_by_prefecture["prefecture_rank"] = mean_by_prefecture.rank(
        ascending=False
    )
    mean_by_prefecture = mean_by_prefecture.sort_values(by="prefecture_rank")
    print("\ntop 5")
    print(mean_by_prefecture.head())
    print("\nbottom 5")
    print(mean_by_prefecture.tail())


if __name__ == "__main__":
    main()
