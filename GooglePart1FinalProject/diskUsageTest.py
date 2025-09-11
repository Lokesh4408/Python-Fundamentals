import shutil
import psutil

def check_disk_usage(disk):
    """Check the disk usage and return True if usage is less than 20%."""
    du = shutil.disk_usage(disk)
    free_percent = du.free / du.total * 100
    return free_percent > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR: Not enough resources")
else:
    print("Everything is OK")
