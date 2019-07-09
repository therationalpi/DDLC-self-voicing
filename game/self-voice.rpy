##This mod enables self-voicing and associated accessibility features for the
##Doki Doki Literature Club game.
define persistent.self_voiced_firstrun = True

python early:
    #Add a new method to Characters to have alternate spoken text for a line
    def alt(self,what,alt_text,interact=True, **kwargs):
        temp_alt=self.what_args['alt']
        self.what_args['alt']=alt_text
        self.__call__(what,interact=interact, **kwargs)
        self.what_args['alt']=temp_alt

    setattr(ADVCharacter, 'alt', alt)

init 10 python:
    # Re-enable accessibility binds if missing
    config.keymap['self_voicing'].append([ 'v', 'V' ])
    config.keymap['clipboard_voicing'].append([ 'C' ])
    config.keymap['debug_voicing'].append([ 'alt_V', 'meta_V' ])

    #If first time running enable self voicing
    if persistent.self_voiced_firstrun:
        preferences.self_voicing = True
        persistent.self_voiced_firstrun = False

    #Add character names to the voicing
    mc.what_args['alt']="I say [text]"
    mc.who_args['alt']=""
    s.what_args['alt']="Sayori says [text]"
    s.who_args['alt']=""
    n.what_args['alt']="Natsuki says [text]"
    n.who_args['alt']=""
    m.what_args['alt']="Monika says [text]"
    m.who_args['alt']=""
    y.what_args['alt']="Yuri says [text]"
    y.who_args['alt']=""
    ny.what_args['alt']="Natsuki and Yuri say [text]"
    ny.who_args['alt']=""
