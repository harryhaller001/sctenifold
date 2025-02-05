from pathlib import Path

import numpy as np
import pandas as pd

from scTenifold import scTenifoldKnk, scTenifoldNet
from scTenifold.data import get_test_df


def test_scTenifoldNet():
    """Testing Net."""
    df_1, df_2 = (
        get_test_df(n_cells=100, n_genes=100),
        get_test_df(n_cells=100, n_genes=100),
    )
    sc = scTenifoldNet(df_1, df_2, "X", "Y", qc_kws={"min_lib_size": 1}, nc_kws={"n_cpus": 1})
    result = sc.build()
    print(result)
    assert isinstance(result, pd.DataFrame)
    sc.save(file_dir="./saved_net")
    _ = scTenifoldNet.load(file_dir="./saved_net")


def test_scTenifoldNet_skip_qc():
    """Testing Net with skipped QC."""
    df_1, df_2 = (
        get_test_df(n_cells=100, n_genes=100),
        get_test_df(n_cells=100, n_genes=100),
    )
    sc = scTenifoldNet(
        df_1,
        df_2,
        "X",
        "Y",
        qc_kws={"min_lib_size": 1, "plot": False},
        nc_kws={"n_cpus": 1},
    )
    result = sc.build()
    print(result)
    assert isinstance(result, pd.DataFrame)
    sc.save(file_dir="./saved_net")
    assert Path("./saved_net/qc/X.csv").is_file()
    assert Path("./saved_net/qc/Y.csv").is_file()

    assert Path("./saved_net/nc/X/network_0.npz").is_file()
    assert Path("./saved_net/nc/Y/network_0.npz").is_file()

    assert Path("./saved_net/td/X.npz").is_file()
    assert Path("./saved_net/td/Y.npz").is_file()

    assert Path("./saved_net/ma/manifold_alignment.csv").is_file()
    assert Path("./saved_net/dr/d_regulation.csv").is_file()

    _ = scTenifoldNet.load(file_dir="./saved_net")


def test_scTenifoldKnk_method1():
    """Testing KNK method 1."""
    df = get_test_df(n_cells=100, n_genes=100, random_state=42)
    sc = scTenifoldKnk(data=df, qc_kws={"min_lib_size": 1})
    sc.run_step("qc")
    sc.run_step("nc", n_cpus=1)
    sc.run_step("td")
    sc.run_step("ko", ko_genes=[sc.tensor_dict["WT"].index.to_list()[0]])
    sc.run_step("ma")
    sc.run_step("dr")
    assert isinstance(sc.d_regulation, pd.DataFrame)
    sc.save(file_dir="./saved_knk")
    sc2 = scTenifoldKnk.load(file_dir="./saved_knk")
    np.array_equal(sc.tensor_dict["WT"], sc2.tensor_dict["WT"])
    assert Path("./saved_knk/qc/WT.csv").is_file()

    assert Path("./saved_knk/nc/WT/network_0.npz").is_file()

    assert Path("./saved_knk/td/WT.npz").is_file()
    assert Path("./saved_knk/td/KO.npz").is_file()

    assert Path("./saved_knk/ma/manifold_alignment.csv").is_file()
    assert Path("./saved_knk/dr/d_regulation.csv").is_file()


def test_scTenifoldKnk_method2():
    """Testing Knk method 2."""
    df = get_test_df(n_genes=100, n_cells=100)
    sc = scTenifoldKnk(
        data=df,
        ko_method="propagation",
        qc_kws={"min_lib_size": 10, "min_percent": 0.001},
        ko_kws={"degree": 10},
    )
    sc.run_step("qc")
    sc.run_step("nc", n_cpus=-1)
    sc.run_step("td")
    sc.run_step("ko", ko_genes=[sc.tensor_dict["WT"].index.to_list()[0]])
    sc.run_step("ma")
    sc.run_step("dr")
    assert isinstance(sc.d_regulation, pd.DataFrame)
