from messages import get_info, get_info_releases, get_film_info_by_id, get_random_film, get_movie_reviews


COMMANDS = {
    0: get_info,
    1: get_random_film,
    2: get_film_info_by_id,
    3: get_info_releases,
    4: get_movie_reviews,
    5: exit
}
