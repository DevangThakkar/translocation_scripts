from Modules import Merger

# Module created using CC_module_helper.py
class Dellymerger(Merger):
	def __init__(self, module_id, is_docker=False):
		super(Dellymerger, self).__init__(module_id, is_docker)
		# Add output keys here if needed
		self.output_keys = ["delly_merged_vcf"]


	def define_input(self):
		# Module creator needs to define which arguments have is_resource=True
		# Module creator needs to rename arguments as required by CC
		self.add_argument("delly_vcf",				is_required=True)
		self.add_argument("sample_id",				is_required=True)
		self.add_argument("nr_cpus",				default_value=2)
		self.add_argument("mem",					default_value=10.0)
		self.add_argument("chr_switch",				default_value=False)
		self.add_argument("chr_filter",				default_value=False)


	def define_output(self):
		# Module creator needs to define what the outputs are
		# based on the output keys provided during module creation
		delly_merged_vcf		= self.generate_unique_file_name("delly.merged.vcf")
		self.add_output("delly_merged_vcf",			delly_merged_vcf)


	def define_command(self):
		# Module creator needs to use renamed arguments as required by CC
		vcf_list				= self.get_argument("delly_vcf")
		sample_id				= self.get_argument("sample_id")
		chr_switch				= self.get_argument("chr_switch")
		chr_filter				= self.get_argument("chr_filter")

		# get output
		delly_merged_vcf		= self.get_output("delly_merged_vcf")

		# add module
		cmd = " python Merge_sample_level_Delly.py"

		# edit sample_id list into one item
		sample_id = '?'.join(sample_id)
		# add arguments
		cmd += " {0} {1} {2} {3}".format(
			delly_merged_vcf, sample_id, chr_switch, chr_filter)

		# add vcf files
		for vcf in vcf_list:
			cmd += " {}".format(vcf)

		# add logging
		cmd += " !LOG3!"

		return cmd