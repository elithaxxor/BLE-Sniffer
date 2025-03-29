interface Device {
    timestamp: string;
    mac_address: string;
    device_name: string;
    vendor: string;
    extra_info: string;
}

document.addEventListener("DOMContentLoaded", () => {
    fetchDevices();
});

function fetchDevices(): void {
    fetch("backend.php")
        .then(response => response.json())
        .then((data: Device[]) => {
            const devicesTable = document.getElementById("devices");
            if (devicesTable) {
                devicesTable.innerHTML = "";
                data.forEach(device => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${device.timestamp}</td>
                        <td>${device.mac_address}</td>
                        <td>${device.device_name}</td>
                        <td>${device.vendor}</td>
                        <td>${device.extra_info}</td>
                    `;
                    devicesTable.appendChild(row);
                });
            }
        })
        .catch(error => console.error("Error fetching devices:", error));
}
