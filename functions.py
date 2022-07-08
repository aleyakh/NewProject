def load_candidates():
    import json
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def get_all():
    all_candidates = load_candidates()
    result = []

    for candidate in all_candidates:
        one_candidate = candidate['name'], candidate['position'], candidate['skills']
        result.append(one_candidate)

    return result

def get_by_pk(pk):
    pk_candidates = load_candidates()
    return pk_candidates[pk-1]

def get_by_skill(sk):
    skill_candidates = load_candidates()
    result = []

    for candidate in skill_candidates:
        if sk.lower() in candidate['skills'].lower():
            one_candidate = candidate['name'], candidate['position'], candidate['skills']
            result.append(one_candidate)

    return result
