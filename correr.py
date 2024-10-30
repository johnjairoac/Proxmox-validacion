from proxmoxer import ProxmoxAPI

# Conectar a Proxmox
proxmox = ProxmoxAPI("192.168.0.251", user="root@pam", password="Deli2022*", verify_ssl=False)
nodo = proxmox.nodes("gestor")

# Iniciar ambas máquinas virtuales
nodo.qemu(100).status.start.post()
nodo.qemu(101).status.start.post()
print("Ambas máquinas virtuales han sido iniciadas.")

# Crear snapshots de ambas máquinas virtuales
nodo.qemu(100).snapshot.post(snapname="snapshot_olympus")
print("Snapshot creado para VM 'olympus'.")

nodo.qemu(101).snapshot.post(snapname="snapshot_omv")
print("Snapshot creado para VM 'OMV'.")

# Consultar el estado de las máquinas virtuales
estado_olympus = nodo.qemu(100).status.current.get()
estado_omv = nodo.qemu(101).status.current.get()
print(f"Estado de 'olympus': {estado_olympus['status']}")
print(f"Estado de 'OMV': {estado_omv['status']}")
