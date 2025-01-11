puts "Setup submodules"

# Clone submodules
system('git clone --branch 1.0.0 --depth 1 https://github.com/SebastianoTaddei/cmake_utils.git cmake_utils')
system('git clone --branch 1.1.1 --depth 1 https://github.com/SebastianoTaddei/GenericContainer.git submodules/GenericContainer')
system('git clone --branch 1.0.1 --depth 1 https://github.com/SebastianoTaddei/UtilsLite.git submodules/UtilsLite')
system('git clone --branch 1.1.1 --depth 1 https://github.com/SebastianoTaddei/quarticRootsFlocke.git submodules/quarticRootsFlocke')

system('ruby submodules/GenericContainer/setup.rb')
system('ruby submodules/UtilsLite/setup.rb')
system('ruby submodules/quarticRootsFlocke/setup.rb')
