"""Shared schema code."""
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.light import ATTR_TRANSITION, ATTR_BRIGHTNESS

CONF_SCHEMA = "schema"
CONF_DEFAULTS = "defaults"
DEFAULT_DEFAULTS = False

MQTT_LIGHT_SCHEMA_SCHEMA = vol.Schema(
    {
        vol.Optional(CONF_SCHEMA, default="basic"): vol.All(
            vol.Lower, vol.Any("basic", "json", "template")
        ),
        vol.Optional(CONF_DEFAULTS, default=DEFAULT_DEFAULTS): vol.Schema(
            {
                vol.Optional(ATTR_TRANSITION): cv.positive_int,
            }
        ),
    }
)
