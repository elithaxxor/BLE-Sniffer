<?php
header("Content-Type: application/json");

$method = $_SERVER['REQUEST_METHOD'];
$db_file = dirname(__FILE__) . "/bluetooth_devices.db";

try {
    $db = new PDO("sqlite:$db_file");
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (Exception $e) {
    echo json_encode(["error" => $e->getMessage()]);
    exit;
}

switch ($method) {
    case 'GET':
        getDevices($db);
        break;
    case 'POST':
        addDevice($db);
        break;
    default:
        echo json_encode(["error" => "Invalid request method"]);
        break;
}

function getDevices($db) {
    $query = "SELECT * FROM devices ORDER BY timestamp DESC";
    $stmt = $db->prepare($query);
    $stmt->execute();
    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
    echo json_encode($result);
}

function addDevice($db) {
    $data = json_decode(file_get_contents('php://input'), true);
    if (!isset($data['mac_address']) || !isset($data['device_name']) || !isset($data['vendor'])) {
        echo json_encode(["error" => "Missing required fields"]);
        return;
    }

    $query = "INSERT INTO devices (timestamp, mac_address, device_name, vendor, extra_info)
              VALUES (:timestamp, :mac_address, :device_name, :vendor, :extra_info)";
    $stmt = $db->prepare($query);
    $stmt->execute([
        ':timestamp' => date('Y-m-d\TH:i:s'),
        ':mac_address' => $data['mac_address'],
        ':device_name' => $data['device_name'],
        ':vendor' => $data['vendor'],
        ':extra_info' => $data['extra_info'] ?? ''
    ]);

    echo json_encode(["success" => "Device added successfully"]);
}
?>
