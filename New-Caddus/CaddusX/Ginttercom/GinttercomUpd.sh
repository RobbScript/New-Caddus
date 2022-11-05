cd ~
mkdir DataCaddus
echo 'Ginttercom - Caddus 2022'
echo 'Mudando locais de Arquivos Salvos...'
cd New-Caddus/New-Caddus/CaddusX/
mv Cad_BNK ~
mv materiasmik ~
mv materiasneil ~
mv UserPass.json ~
mv Cad_BNK DataCaddus
mv materiasmik DataCaddus
mv materiasneil DataCaddus
mv UserPass.json DataCaddus
echo '|Locais Editados|'
echo 'Removendo Caddus Antigo...'
cd ~
sudo rmdir New-Caddus
echo '|Caddus Antigo Removido|'
echo 'Atualizando Caddus...'
git clone https://github.com/RobbScript/New-Caddus
echo '|Caddus Atualizado|'
echo 'Movendo Dados Salvos...'
cd DataCaddus
mv Cad_BNK ~
mv materiasmik ~
mv materiasneil ~
mv UserPass.json ~
mv Cad_BNK New-Caddus/New-Caddus/CaddusX/
mv materiasmik New-Caddus/New-Caddus/CaddusX/
mv materiasneil New-Caddus/New-Caddus/CaddusX/
mv UserPass.json New-Caddus/New-Caddus/CaddusX/
echo '|Dados Antigos Salvos|'
echo 'Pronto'
