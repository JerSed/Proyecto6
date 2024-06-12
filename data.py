headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Said",
    "phone": "+34579435721",
    "address": "8764 Grand Central Terminal, NY"
}


def kit_payloads(one_character):
    return kit_bodies[one_character].copy()


kit_bodies = {
    "one_character": {"name": "a"},
    "maximum_characters": {"name": ("Abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdAbcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdab"
                                    "cdabcdabcdabcdabcdabcdabcdabcdabcd"
                                    "abcdabcdabcdabcdabcdabcdabcdabcdabC")},
    "empty_string": {"name": ""},
    "maximum_plus_one_characters": {"name": ("Abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdAbcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabcdabcdabcd"
                                             "abcdabcdabcdabcdabcdabcdab"
                                             "cdabcdabcdabcdabC")},
    "special_characters": {"name": '"№%@"'},
    "spaces": {"name": " A Aaa "},
    "numbers": {"name": "123"},
    "empty_kit_body": {},
    "number_name": {"name": 123}
}
