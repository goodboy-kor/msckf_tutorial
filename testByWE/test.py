import logging
import click

logger = logging.getLogger(__name__)

LEFT_CAMERA_FOLDER = "cam0"
RIGHT_CAMERA_FOLDER = "cam1"
IMU_FOLDER = "imu0"
GT_FOLDER = "state_groundtruth_estimate0"
DATA_FILE = "data.csv"

TIMESTAMP_INDEX = 0

NANOSECOND_TO_SECOND = 1e-9
