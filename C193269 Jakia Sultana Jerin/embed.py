def embed_meeting(meeting_id):
  # generate the embed code for the meeting
  embed_code = f'<iframe allow="camera; microphone; fullscreen; display-capture; autoplay" src="https://meet.jit.si/StandardAdministratorsDreamThereby" style="height: 100%; width: 100%; border: 0px;"></iframe>'

  # render the view with the embed code
  return render_template('meeting.html', embed_code=embed_code)