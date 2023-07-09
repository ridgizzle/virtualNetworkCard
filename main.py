# TODO: Selenium um Webserver zu interargieren
# TODO: Ergebnisse in Exceldatei printen

import pydivert


def order_file_alphabetically(file_path):
    # Read the contents of the file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Sort the lines based on IP addresses
    sorted_lines = sorted(lines, key=lambda line: [int(octet) for octet in line.strip().split('.')])

    # Write the sorted lines back to the file
    with open(file_path, "w") as file:
        file.writelines(sorted_lines)


def protcol_documenter(protocol):
    # Open the file in read mode
    with open(f"testing_results/{protocol}.txt", "r") as file:
        # Read the contents of the file
        file_contents = file.read()

    # Check if the variable is present in the file
    if packet.dst_addr not in file_contents:
        # Open the file in append mode
        with open(f"testing_results/{protocol}.txt", "a") as file:
            # Write the variable's value to the file
            file.write(packet.dst_addr + "\n")


# SYSLOG und NTP Packets auslesen
with pydivert.WinDivert("udp.DstPort == 514 or udp.DstPort == 123") as w:
    for packet in w:
        # Pakete werden hier geprinted und weitergeleitet
        print(packet)
        print("\n\n#####################################\n\n")
        w.send(packet)

        # Überprüfung auf Projektrelevante Pakete
        if packet.dst_port == 514:
            protcol_documenter("SYSLOG")
        if packet.dst_port == 123:
            protcol_documenter("NTP")
        # TODO: RADIUS und SNMP überprüfen

        order_file_alphabetically("testing_results/SYSLOG.txt")
