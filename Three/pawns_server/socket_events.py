from enum import Enum


class SocketEvents(Enum):
    CONNECT = 'connect',
    DISCONNECT = 'disconnect',
    SET_COLOR = 'set_color',
    GET_COLOR = 'get_color',
    SET_GAME_STATE = 'set_game_state',
    GET_GAME_STATE = 'get_game_state',
    DO_MOVE = 'do_move',
    PLAYER_DISCONNECTED = 'player_disconnected',
    GAME_FINISHED = 'game_finished',
    GAME_RESTARTED = 'game_restarted'
