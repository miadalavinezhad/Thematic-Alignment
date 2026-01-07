import pandas as pd


def yearly_alignment(papers_df: pd.DataFrame, rolling: int=None) -> pd.DataFrame:
    """
    Analyze the trend of thematic alignment scores over the years.
    """
    if rolling:
        return (
            papers_df["mean_alignment_score"]
            .rolling(window=rolling, center=True)
            .mean()
        )
    
    return (
        papers_df.groupby("year")["alignment_score"]
        .mean()
        .reset_index(name='mean_alignment_score')
    )