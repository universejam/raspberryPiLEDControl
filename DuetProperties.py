class DuetProperties:
    status = None
    heater1 = None
    heater2 = None
    heater1_active = None
    heater2_active = None
    heater1_standby = None
    heater2_standby = None
    heater1_status = None
    heater2_status = None
    xPosition = None
    yPosition = None
    zHeight = None
    speedFactor = None
    babystep = None
    tool = None
    probe = None
    fan1_percent = None
    fan2_percent = None
    fan3_percent = None
    printCoolingFan_RPM = None
    xHomedStatus = None
    yHomedStatus = None
    zHomedStatus = None

    # {'status': 'I', 'heaters': [24.2, 23.8], 'active': [0.0, 0.0], 'standby': [0.0, 0.0], 'hstat': [0, 0],
    # 'pos': [0.0, 0.0, 333.5], 'sfactor': 100.0, 'efactor': [100.0], 'babystep': 0.0, 'tool': -1, 'probe': '0',
    # 'fanPercent': [53.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'fanRPM': 0, 'homed': [0, 0, 0], 'msgBox.mode': -1}

    def __init__(self):
        pass
