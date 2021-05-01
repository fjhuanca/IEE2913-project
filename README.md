# Instrucciones

## Primero instalar ESPTool
`pip install --upgrade esptool`

## Instalar en VSCode Pymakr
Puede ser algún otro programa similar también.

## Configurar la ESP con MicroPython

### Borrar la memoria flash
`esptool.py --chip esp32 -p <USB-to-Serial Port> erase_flash`

### Cargarle el archivo .bin
`esptool.py --chip esp32 -p <USB-to-Serial Port> write_flash -z 0x1000 <path to .bin>`

### Configurar la conexión con la ESP (asignar el puerto COM).
