def add_reaction(shortcut_name, reaction):
  # check if the shortcut exists in the database
  shortcut = Shortcut.query.filter_by(name=shortcut_name).first()
  if shortcut:
    # check if the reaction is valid
    if reaction not in ['love', 'surprised', 'boo', 'sad']:
      return 'Invalid reaction'
    
    # add the reaction to the shortcut
    if reaction == 'love':
      shortcut.love_count += 1
    elif reaction == 'surprised':
      shortcut.surprised_count += 1
    elif reaction == 'boo':
      shortcut.boo_count += 1
    else:
      shortcut.sad_count += 1
    
    # commit the changes to the database
    db.session.commit()
    
    return 'Reaction added successfully'
  else:
    # handle the case where the shortcut does not exist
    return 'Shortcut not found'
