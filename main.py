import pm4py
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.filtering.log.variants import variants_filter
from pm4py.algo.enhancement.sna import algorithm as sna
from pm4py.visualization.sna import visualizer as sna_visualizer


log = xes_importer.apply(r'C:\Users\HAXY8W\Desktop\Process Mining\Audit Process Mining\financial_log.xes.gz')
filtered_log1 = variants_filter.apply(log, {'A_SUBMITTED,A_PARTLYSUBMITTED,A_DECLINED'},
                                      parameters={variants_filter.Parameters.POSITIVE: False})

# part of the analysis was to eliminate unwanted actions, the code below does just that.
# it is not needed to run the network however if you want to filter these activities out: uncomment it and then change
# the name in network algo sections from filtered_log1 to filtered_log2

# event_log1 = pm4py.convert_to_event_stream(filtered_log1)
# filtered_log2 = pm4py.filtering.filter_event_attribute_values(filtered_log1, 'concept:name',
#                                                               {"O_SELECTED", "O_CREATED", "O_ACCEPTED",
#                                                                "A_REGISTERED", "A_ACTIVATED",
#                                                                "O_CANCELLED", "O_DECLINED", 'A_PARTLYSUBMITTED'},
#                                                               level='event', retain=False)



# Network algorithm sections

# Handover of Work
hw_values = sna.apply(filtered_log1, variant=sna.Variants.HANDOVER_LOG)
gviz_hw_py = sna_visualizer.apply(hw_values, variant=sna_visualizer.Variants.PYVIS)
sna_visualizer.view(gviz_hw_py, variant=sna_visualizer.Variants.PYVIS)

# Subcontracting
# sub_values = sna.apply(filtered_log2, variant=sna.Variants.SUBCONTRACTING_LOG)
# gviz_sub_py = sna_visualizer.apply(sub_values, variant=sna_visualizer.Variants.PYVIS)
# sna_visualizer.view(gviz_sub_py, variant=sna_visualizer.Variants.PYVIS)

# Working Together
# wt_values = sna.apply(filtered_log2, variant=sna.Variants.WORKING_TOGETHER_LOG)
# gviz_wt_py = sna_visualizer.apply(wt_values, variant=sna_visualizer.Variants.PYVIS)
# sna_visualizer.view(gviz_wt_py, variant=sna_visualizer.Variants.PYVIS)


