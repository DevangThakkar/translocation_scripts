from Modules import Merger

# Module created using CC_module_helper.py
class Dellylumpydestruct_anno_merger(Merger):
	def __init__(self, module_id, is_docker=False):
		super(Dellylumpydestruct_anno_merger, self).__init__(module_id, is_docker)
		# Add output keys here if needed
		self.output_keys = ["anno_vcf"]


	def define_input(self):
		# Module creator needs to define which arguments have is_resource=True
		# Module creator needs to rename arguments as required by CC
		self.add_argument("all_merged_vcf",			is_required=True)
		self.add_argument("bed",					is_resource=True)
		self.add_argument("dac_gap_blacklist",		is_resource=True)
		self.add_argument("repeat_blacklist",		is_resource=True)
		self.add_argument("level1_bp",				is_resource=True)
		self.add_argument("gtf",					is_resource=True)
		self.add_argument("paper_freq_pairs",		is_resource=True)
		self.add_argument("nr_cpus",				default_value=2)
		self.add_argument("mem",					default_value=10.0)
		self.add_argument("chr_filter",				default_value=0)


	def define_output(self):
		# Module creator needs to define what the outputs are
		# based on the output keys provided during module creation
		anno_vcf						= self.generate_unique_file_name("anno.vcf")
		self.add_output("anno_vcf",					anno_vcf)


	def define_command(self):
		# Module creator needs to use renamed arguments as required by CC
		all_merged_vcf					= self.get_argument("all_merged_vcf")
		bed								= self.get_argument("bed")
		dac_gap_blacklist				= self.get_argument("dac_gap_blacklist")
		repeat_blacklist				= self.get_argument("repeat_blacklist")
		level1_bp						= self.get_argument("level1_bp")
		gtf								= self.get_argument("gtf")
		paper_freq_pairs				= self.get_argument("paper_freq_pairs")
		chr_filter						= self.get_argument("chr_filter")

		# get output
		anno_vcf						= self.get_output("anno_vcf")

		# add module
		cmd = " python Merge_delly_lumpy_destruct_annotation.py"

		# add arguments
		cmd += " {0} {1} {2}".format(all_merged_vcf, sample_id, chr_filter)

		# add merged vcf files
		cmd += " {0} {1} {2}".format(delly_file, lumpy_file, destruct_file)

		# add logging
		cmd += " !LOG3!"

		return cmd