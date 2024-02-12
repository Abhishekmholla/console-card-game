def get_replaced_character(character):
    """
        This function replaces the character with a specific value

        Parameters:
        :param character: Refers to a specific character

        Returns:
        Returns the character value
        """
    # If the character is any of A,J,Q and K, 
    # then replacing it there corresponding values
    if character.lower() == 'a':
        character = character.replace(character, '1')
    elif character.lower() == 'j':
        character = character.replace(character, '11')
    elif character.lower() == 'q':
        character = character.replace(character, '12')
    elif character.lower() == 'k':
        character = character.replace(character, '13')
    return character