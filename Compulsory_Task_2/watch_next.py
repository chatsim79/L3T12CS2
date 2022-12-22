# importing spacy
import spacy  
# specifying md model as we want to use word vectors.
nlp = spacy.load('en_core_web_md')


def reccomend(desc):
    """
    This method will be used to compare the semantic 
    similarity (using word vectors) of a list of movie 
    descriptions to a reference description in order 
    to reccommend a movie to the viewer.

    :param str desc: The reference description

    :returns: The most semantically similar movie on the list

    :rtype: str
    """

    # Create dictionary of movie descriptions against similarity index
    movie_sim = {}
    # Tokenise/call nlp on reference description
    model_desc = nlp(desc)
    with open('movies.txt','r',encoding='utf-8') as f:
        for line in f:
            # Call comparison on line and ref description
            similarity = nlp(line).similarity(model_desc)
            # Write line and similarity index to dictionary
            movie_sim[line] = similarity
    # Get and return line with highest similarity index to reference description.
    sim_max = max(movie_sim, key=movie_sim.get)
    return sim_max
    

ref_desc = (
"""
Planet Hulk:
Will he save their world or destroy it? When the Hulk becomes 
too dangerous for the Earth, the Illuminati trick Hulk into a 
shuttle and launch him into space to a planet where the Hulk 
can live in peace. Unfortunately, Hulk land on the planet Sakaar 
where he is sold into slavery and trained as a gladiator.
"""
           )
print(f"\n{reccomend(ref_desc)}")
