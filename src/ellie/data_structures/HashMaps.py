from typing import List


def findRelativeRanks(self, score: List[int]) -> List[str]:
    """findRelativeRanks
    Description
    -----------
    506. Relative Ranks
    This function set rank of athletes based on their scores.  All the scores are guaranteed to be unique.

    Parameters
    ----------
    score : List[int]
         score[i] is the score of the ith athlete in a competition

    Returns
    -------
    List[str]
        rank of i-th athlete
    Example
    -------
    >>> findRelativeRanks(score=[10,3,8,9,4])
    >>> ["Gold Medal","5","Bronze Medal","Silver Medal","4"]   
    """
    scores_position_map={}
    medals=["Gold Medal","Silver Medal","Bronze Medal"]
    sorted_scored=sorted(score,reverse=True)
    for i,s in enumerate(sorted_scored):
        scores_position_map[s]=i
    results=[]
    for i in score:
        if scores_position_map[i]==0:
            rank="Gold Medal"  
            results.append(rank)  
        elif scores_position_map[i]==1:
            rank="Silver Medal"
            results.append(rank)
        elif scores_position_map[i]==2:
            rank="Bronze Medal"   
            results.append(rank) 
        else:
            rank = str(scores_position_map[i]+1)
            results.append(rank)
    print(scores_position_map)        
    return results



