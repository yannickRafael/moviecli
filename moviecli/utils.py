def format_search_results_into_choices(search_results):
    choices = []
    for i, result in enumerate(search_results, start=1):
        title = result[0]
        url = result[1]
        year = result[3]
        choice = f'{i}. {title} ({year})'
        choices.append(choice)
    return choices
