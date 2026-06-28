from __future__ import annotations

from enum import StrEnum

TWO_DIGIT_YEAR = "26"
YEAR = "2026"


class SystemConsole(StrEnum):
    XBOX_ONE = "xone"
    PS4 = "ps4"
    PC = "pc"
    PS5 = "ps5"
    XBOX_X = "xbsx"
    STADIA = "stadia"


class ConsoleOverride(StrEnum):
    NONE = "Default"
    XBOX_ONE = "Xbox One"
    PS4 = "PS4"
    PC = "PC"
    PS5 = "PS5"
    XBOX_X = "XBOX Series X"
    STADIA = "Stadia"


class Stage:
    UNKNOWN = -1
    PRESEASON = 0
    SEASON = 1


VALID_ENTITLEMENTS = {
    SystemConsole.XBOX_ONE: f"MADDEN_{TWO_DIGIT_YEAR}XONE",
    SystemConsole.PS4: f"MADDEN_{TWO_DIGIT_YEAR}PS4",
    SystemConsole.PC: f"MADDEN_{TWO_DIGIT_YEAR}PC",
    SystemConsole.PS5: f"MADDEN_{TWO_DIGIT_YEAR}PS5",
    SystemConsole.XBOX_X: f"MADDEN_{TWO_DIGIT_YEAR}XBSX",
    SystemConsole.STADIA: f"MADDEN_{TWO_DIGIT_YEAR}SDA",
}

ENTITLEMENT_TO_SYSTEM = {
    entitlement: console for console, entitlement in VALID_ENTITLEMENTS.items()
}

CONSOLE_OVERRIDE_TO_ENTITLEMENT = {
    ConsoleOverride.XBOX_ONE: f"MADDEN_{TWO_DIGIT_YEAR}XONE",
    ConsoleOverride.PS4: f"MADDEN_{TWO_DIGIT_YEAR}PS4",
    ConsoleOverride.PC: f"MADDEN_{TWO_DIGIT_YEAR}PC",
    ConsoleOverride.PS5: f"MADDEN_{TWO_DIGIT_YEAR}PS5",
    ConsoleOverride.XBOX_X: f"MADDEN_{TWO_DIGIT_YEAR}XBSX",
    ConsoleOverride.STADIA: f"MADDEN_{TWO_DIGIT_YEAR}SDA",
}

CONSOLE_OVERRIDE_TO_VALID_NAMESPACE = {
    ConsoleOverride.XBOX_ONE: "xbox",
    ConsoleOverride.PS4: "ps3",
    ConsoleOverride.PC: "cem_ea_id",
    ConsoleOverride.PS5: "ps3",
    ConsoleOverride.XBOX_X: "xbox",
    ConsoleOverride.STADIA: "stadia",
}

SYSTEM_MAP = {
    SystemConsole.XBOX_ONE: f"MADDEN_{TWO_DIGIT_YEAR}_XONE_BLZ_SERVER",
    SystemConsole.PS4: f"MADDEN_{TWO_DIGIT_YEAR}_PS4_BLZ_SERVER",
    SystemConsole.PC: f"MADDEN_{TWO_DIGIT_YEAR}_PC_BLZ_SERVER",
    SystemConsole.PS5: f"MADDEN_{TWO_DIGIT_YEAR}_PS5_BLZ_SERVER",
    SystemConsole.XBOX_X: f"MADDEN_{TWO_DIGIT_YEAR}_XBSX_BLZ_SERVER",
    SystemConsole.STADIA: f"MADDEN_{TWO_DIGIT_YEAR}_SDA_BLZ_SERVER",
}

BLAZE_SERVICE = {
    SystemConsole.XBOX_ONE: f"madden-{YEAR}-xone",
    SystemConsole.PS4: f"madden-{YEAR}-ps4",
    SystemConsole.PC: f"madden-{YEAR}-pc",
    SystemConsole.PS5: f"madden-{YEAR}-ps5",
    SystemConsole.XBOX_X: f"madden-{YEAR}-xbsx",
    SystemConsole.STADIA: f"madden-{YEAR}-stadia",
}

BLAZE_PRODUCT_NAME = {
    SystemConsole.XBOX_ONE: f"madden-{YEAR}-xone-mca",
    SystemConsole.PS4: f"madden-{YEAR}-ps4-mca",
    SystemConsole.PC: f"madden-{YEAR}-pc-mca",
    SystemConsole.PS5: f"madden-{YEAR}-ps5-mca",
    SystemConsole.XBOX_X: f"madden-{YEAR}-xbsx-mca",
    SystemConsole.STADIA: f"madden-{YEAR}-stadia-mca",
}
