import requests
from tqdm import tqdm
import time
import pandas as pd


def is_valid_paper(paper: dict) -> bool:
    """
    Check whether the venue string is associated to
    PLOS Computational Biology.
    """

    p_venue = paper.get("venue")
    if not p_venue:
        return False

    p_venue = p_venue.lower()
    return ('comutational' in p_venue or 'comput' in p_venue) and \
            ('biology' in p_venue or 'biol' in p_venue) and \
            ('plos' in p_venue) and \
            paper.get("abstract") is not None


def fetch_papers(
        query: str,
        fields: list[str],
        headers: dict[str, str],
        url: str,
        max_papers: int=1000, 
        batch_size: int=50, 
        sleep_time: float=1.5
    ) -> pd.DataFrame:
    """
    Fetch papers from Semantic Scholar and filter by venue.
    """

    papers = []
    offset = 0

    with tqdm(total=max_papers, desc="num. of papers fetched") as pbar:
        while len(papers) < max_papers and offset < 1000: # offset more than 1000 is not allowed in the API
            params = {
                "query": query,
                "limit": batch_size,
                "offset": offset,
                "fields": ",".join(fields)
            }

            # Send request to API
            response = requests.get(
                url=url, 
                params=params, 
                headers=headers
                )
            response.raise_for_status()
            data = response.json()
            
            # Check for empty data
            if "data" not in data or len(data["data"]) == 0:
                break

            for paper in data["data"]:
                if is_valid_paper(paper):
                    papers.append({
                        "title": paper["title"],
                        "abstract": paper["abstract"],
                        "year": paper["year"],
                        "venue": paper["venue"]
                    })
                    pbar.update(1)

                if len(papers) >= max_papers:
                    break

            offset += batch_size
            time.sleep(sleep_time)

    return pd.DataFrame(papers)