import logging

# Used AI for comments, debugging assistance and optimization

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Device:
    # Represents an IoT device with its security attributes.
    def __init__(self, device_id, device_type, ip_address, mac_address, firmware_version):
        self.device_id = device_id
        self.device_type = device_type
        self.ip_address = ip_address
        self.mac_address = mac_address
        self.firmware_version = firmware_version
        self.is_compliant = False
        self.allowed_users = set()

    def __repr__(self):
        return f"Device(id={self.device_id}, type={self.device_type}, ip={self.ip_address})"

class User:
    # Represents a user with specific permissions.
    def __init__(self, user_id, username, permissions=None):
        self.user_id = user_id
        self.username = username
        self.permissions = permissions or []

    def __repr__(self):
        return f"User(id={self.user_id}, name={self.username})"

class IoTDeviceManager:
    # Manages IoT devices and user interactions in the network.
    def __init__(self, required_firmware_versions=None):
        self.devices = {}
        self.users = {}
        self.required_firmware_versions = required_firmware_versions or {}
        logging.info("IoT Device Manager initialized.")

    def add_device(self, device):
        # Adds a new device to the manager and checks its compliance.
        if device.device_id not in self.devices:
            self.devices[device.device_id] = device
            self.check_compliance(device)
            logging.info(f"Added device: {device}")
        else:
            logging.warning(f"Device with ID {device.device_id} already exists.")

    def add_user(self, user):
        # Adds a new user to the manager.
        if user.user_id not in self.users:
            self.users[user.user_id] = user
            logging.info(f"Added user: {user}")
        else:
            logging.warning(f"User with ID {user.user_id} already exists.")

    def check_compliance(self, device):
        # Checks if a device is compliant with security policies.
        required_version = self.required_firmware_versions.get(device.device_type)
        if required_version and device.firmware_version >= required_version:
            device.is_compliant = True
            logging.info(f"Device {device.device_id} is compliant.")
        else:
            device.is_compliant = False
            logging.warning(f"Device {device.device_id} is NOT compliant. "
                            f"Required firmware: {required_version}, "
                            f"has: {device.firmware_version}")
        return device.is_compliant

    def grant_access(self, user_id, device_id):
        # Grants a user access to a specific device.
        if user_id in self.users and device_id in self.devices:
            self.devices[device_id].allowed_users.add(user_id)
            logging.info(f"Access granted for user {user_id} to device {device_id}.")
        else:
            logging.error("User or device not found.")

    def revoke_access(self, user_id, device_id):
        # Revokes a user's access from a specific device.
        if user_id in self.users and device_id in self.devices:
            self.devices[device_id].allowed_users.discard(user_id)
            logging.info(f"Access revoked for user {user_id} from device {device_id}.")
        else:
            logging.error("User or device not found.")

    def interact(self, user_id, device_id, action):
        # Allows a user to interact with a device, after checking for authorization and compliance.
        user = self.users.get(user_id)
        device = self.devices.get(device_id)

        if not user or not device:
            logging.error(f"Interaction failed: User {user_id} or Device {device_id} not found.")
            return

        if not device.is_compliant:
            logging.warning(f"Interaction DENIED: Device {device.device_id} is not compliant.")
            return

        if user_id not in device.allowed_users and 'admin' not in user.permissions:
            logging.warning(f"Interaction DENIED: User {user.username} is not authorized "
                            f"to interact with device {device.device_id}.")
            return

        logging.info(f"User {user.username} successfully performed action '{action}' "
                     f"on device {device.device_id}.")
        # In a real system, this is where you would send a command to the device.
        print(f"  -> Action '{action}' on device {device.device_id} was successful.\n")


if __name__ == '__main__':
    # Define required firmware versions for compliance
    required_firmware = {
        "thermostat": "2.1.0",
        "camera": "1.5.2",
        "light_bulb": "1.0.0"
    }

    # Initialize the manager
    manager = IoTDeviceManager(required_firmware)

    # Create users
    admin_user = User("admin01", "Alice", permissions=['admin'])
    regular_user = User("user01", "Bob")
    
    manager.add_user(admin_user)
    manager.add_user(regular_user)

    # Create devices
    compliant_camera = Device("cam01", "camera", "192.168.1.10", "00-1A-2B-3C-4D-5E", "1.6.0")
    non_compliant_thermostat = Device("therm01", "thermostat", "192.168.1.11", "00-1A-2B-3C-4D-5F", "2.0.0")
    
    manager.add_device(compliant_camera)
    manager.add_device(non_compliant_thermostat)

    # Grant access to Bob for the compliant camera
    manager.grant_access(regular_user.user_id, compliant_camera.device_id)

    print("\n--- Testing Interactions ---\n")

    # 1. Admin tries to access the compliant camera (should succeed due to admin rights)
    manager.interact(admin_user.user_id, compliant_camera.device_id, "view_stream")

    # 2. Bob tries to access the compliant camera (should succeed as he has been granted access)
    manager.interact(regular_user.user_id, compliant_camera.device_id, "view_stream")

    # 3. Bob tries to access the non-compliant thermostat (should be denied)
    manager.interact(regular_user.user_id, non_compliant_thermostat.device_id, "set_temperature")

    # 4. Admin tries to access the non-compliant thermostat (should be denied due to non-compliance)
    manager.interact(admin_user.user_id, non_compliant_thermostat.device_id, "set_temperature")
    
    # 5. Revoke Bob's access and try again (should be denied)
    manager.revoke_access(regular_user.user_id, compliant_camera.device_id)
    manager.interact(regular_user.user_id, compliant_camera.device_id, "view_stream")
