import sys
import tracemalloc
from collections.abc import Callable


class FirstExperimentResult:
    def __init__(
        self,
        name: str,
        count: int,
        object_size: int, 
        current_memory: int,
        peak_memory: int
    ):
        self.name = name
        self.count = count
        self.object_size = object_size
        self.current_memory = current_memory
        self.peak_memory = peak_memory

class SecondExperimentResult:
    def __init__(
        self,
        count: int,
        list_size: int,
    ):
        self.count = count
        self.list_size = list_size

class ThirdExperimentResult:
    def __init__(
        self,
        name: str,
        current_memory: int,
        peak_memory: int
    ):
        self.current_memory = current_memory
        self.peak_memory = peak_memory
        self.name = name


def get_first_experiment_result(
        name: str,
        count: int,
        factory: Callable
    ) -> FirstExperimentResult:
    tracemalloc.start()

    obj = factory()
    current, peak = tracemalloc.get_traced_memory()
    object_size = sys.getsizeof(obj)

    tracemalloc.stop()

    result = FirstExperimentResult(
        name=name,
        count=count,
        object_size=object_size,
        current_memory=current,
        peak_memory=peak
    )

    del obj
    return result

def get_growing_list_history() -> dict:
    result = {
        "history": [],
        "peak_memory": None,
        "current_memory": None
    }

    tracemalloc.start()

    arr = []
    prev_size = sys.getsizeof(arr)

    for i in range(100):
        arr.append(i)
        current_size = sys.getsizeof(arr)

        if current_size != prev_size:
            result["history"].append(
                SecondExperimentResult(
                    count=i,
                    list_size=current_size
                )
            )
            prev_size = current_size

    current, peak = tracemalloc.get_traced_memory()
    result["current_memory"] = current
    result["peak_memory"] = peak

    tracemalloc.stop()

    return result

def get_third_experiment_result() -> dict:
    result = {
        "list": None,
        "range": None
    }
    tracemalloc.start()

    numbers = list(range(100_000))

    current, peak = tracemalloc.get_traced_memory()
    result["list"] = ThirdExperimentResult(
        name="список из 100000 элементов",
        current_memory=current,
        peak_memory=peak
    )

    tracemalloc.stop()
    tracemalloc.start()

    numbers = range(100_000)

    current, peak = tracemalloc.get_traced_memory()
    result["range"] = ThirdExperimentResult(
        name="объект range(100_000)",
        current_memory=current,
        peak_memory=peak
    )

    tracemalloc.stop()

    return result

def print_report(result: dict) -> None:
    print("================= Размер отдельных объектов =================\n")

    for obj_data in result["experiment_1"]:
        print(
            f"{obj_data.name}:\n\n"
            f"  - кол-во элементов:  {obj_data.count}\n"
            f"  - размер внешнего объекта:  {obj_data.object_size}\n"
            f"  - текущее использование памяти: {obj_data.current_memory} байт\n"
            f"  - максимальное использование памяти: {obj_data.peak_memory} байт\n"            
        )


    print("======================= Рост списка ========================\n")
    print(
        f"максимальное использование памяти: {result['experiment_2']["peak_memory"]} байт\n\n"
        f"текущее использование памяти: {result['experiment_2']["current_memory"]} байт\n\n"
        f"история изменения размера списка:\n",
        f"____________________________________________________\n"
        f"| кол-во элементов в списке | размер списка (в байт) |\n"
        f"|___________________________|________________________|"
    )

    for obj_data in result["experiment_2"]["history"]:
        print(
            f"|{obj_data.count:^27}|{obj_data.list_size:^24}|\n"
            f"|___________________________|________________________|"
        )


    print("\n=============== Измерение через tracemalloc ================\n")

    list_obj_data: ThirdExperimentResult = result['experiment_3']["list"]
    range_obf_data: ThirdExperimentResult = result['experiment_3']["range"]
    print(
        f"{list_obj_data.name}:\n\n"
        f"  - текущее использование памяти: {(list_obj_data.current_memory / 1000):.2f} Кбайт\n"
        f"  - максимальное использование памяти: {(list_obj_data.peak_memory / 1000):.2f} Кбайт\n\n"
        f"{range_obf_data.name}:\n\n"
        f"  - текущее использование памяти: {(range_obf_data.current_memory / 1000):.2f} Кбайт\n"
        f"  - максимальное использование памяти: {(range_obf_data.peak_memory / 1000):.2f} Кбайт\n\n"
        f"отношение пиковых объемов двух сравниваемых сценариев: {(list_obj_data.peak_memory / range_obf_data.peak_memory):.2f}"
    )
    

result = {
    "experiment_1": [],
    "experiment_2": None,
    "experiment_3": None
}


# Часть 1
result_first_experiment: list[FirstExperimentResult] = []

scenarios_first_experiment = [
    dict(
        name="пустой список",
        count=0,
        factory=lambda: []
    ),
    dict(
        name="список из десяти целых чисел",
        count=10,
        factory=lambda: list(range(390, 400))        
    ),
    dict(
        name="кортеж из десяти целых чисел",
        count=10,
        factory=lambda: tuple(list(range(390, 400)))       
    ),
    dict(
        name="строка из десяти символов",
        count=10,
        factory=lambda: "abcdefghij"      
    ),
    dict(
        name="целое число",
        count=1,
        factory=lambda: 333      
    ),
    dict(
        name="объект None",
        count=0,
        factory=lambda: None     
    ),
]

for scenario in scenarios_first_experiment:
    result["experiment_1"].append(
        get_first_experiment_result(**scenario)
    )

# Часть 2
result["experiment_2"] = get_growing_list_history()

# Часть 3
result["experiment_3"] = get_third_experiment_result()

# Печать отчета
print_report(result)