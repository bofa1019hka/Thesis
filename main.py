from processing.pipeline import run_pipeline


def main():
    print("Pipeline starten")

    data = run_pipeline(limit=100)

    print("Pipeline abgeschlossen")

    print("\nAusgabe:")
    for i, entry in enumerate(data[:3], 1):
        print(f"\nDatensatz {i}")
        for key, value in entry.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
