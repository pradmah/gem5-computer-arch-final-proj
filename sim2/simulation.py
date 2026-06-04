from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_shared_l2_walk_cache_hierarchy import PrivateL1SharedL2WalkCacheHierarchy
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.processors.cpu_types import CPUTypes
from gem5.isas import ISA
from gem5.resources.resource import obtain_resource, Resource
from gem5.simulate.simulator import Simulator

cache =PrivateL1CacheHierarchy("32KiB", "32KiB")

memory = SingleChannelDDR4_2400("2GiB")
processor_inorder = SimpleProcessor(CPUTypes.TIMING,1, ISA.X86)
board = SimpleBoard("3GHz", processor_inorder, memory, cache)
board.set_workload(obtain_resource("x86-matrix-multiply-run"))

sim = Simulator(board)

sim.run()
