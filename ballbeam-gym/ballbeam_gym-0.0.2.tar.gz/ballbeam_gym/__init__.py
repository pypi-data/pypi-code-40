from gym.envs.registration import register

register(
    id='BallBeamBalance-v0',
    entry_point='ballbeam_gym.envs:BallBeamBalanceEnv',
)

register(
    id='VisualBallBeamBalance-v0',
    entry_point='ballbeam_gym.envs:VisualBallBeamBalanceEnv',
)

register(
    id='BallBeamSetpoint-v0',
    entry_point='ballbeam_gym.envs:BallBeamSetpointEnv',
)

register(
    id='VisualBallBeamSetpoint-v0',
    entry_point='ballbeam_gym.envs:VisualBallBeamSetpointEnv',
)
