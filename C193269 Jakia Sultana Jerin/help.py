def display_help():
  # retrieve the list of available commands from a database or configuration file
  commands = get_commands()

  # render the help template with the list of commands
  return render_template('help.html', commands=commands)