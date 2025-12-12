# MFNOD

Qilin Lia, Rui Wanga, Sihan Wang, Luoshu Yang, Dezhong Peng, Zhong Yuan, **Xiniyu Su***, [Multi-granularity fuzzy neighborhood-based outlier detection](https://doi.org/10.1016/j.ins.2025.122983), Information Sciences, 2025.

## Abstract
Unsupervised outlier detection aims to identify samples that significantly deviate from normal patterns by leveraging the inherent information within the data, without relying on labeled guidance. {Density-based outlier detection methods employ various density metrics to evaluate and determine how anomalous a sample is by leveraging the neighborhood density information of samples.} Despite their effectiveness, most rely on deterministic density estimation, neglecting data uncertainty, which can lead to misclassification of normal and abnormal samples. Additionally, they often overlook multi-granularity information, limiting their ability to capture complex data structures. In this study, we propose the Multi-granularity Fuzzy Neighborhood Outlier Detection (MFNOD), which measures the degree to which samples are outliers using the density of their multi-granularity fuzzy neighborhoods. Within MFNOD, we first employ a kernelized fuzzy relation to characterize complex relationships between samples. {To better capture the multi-granularity characteristics present in the data,} we introduce varying bandwidths for the kernelized fuzzy relation, {thereby defining} novel multi-granularity kernelized fuzzy relations. Based on the new fuzzy relations, we construct multi-granularity kernelized fuzzy neighborhood granules for each sample. Utilizing these information granules, we compute the multi-granularity kernelized fuzzy neighborhood density for each sample and compare its density with the densities of its neighbors to compute the final outlier scores. Experiments conducted with 13 methods across 24 datasets demonstrate that MFNOD achieves superior outlier detection performance, validating its effectiveness.

## Citation
If you find GBDO useful in your research, please consider citing:
```

```
## Contact
If you have any questions, please contact suxinyu@stu.scu.edu.cn.



