function reformatDate(date: string): string {
    const months: Record<string, string> = {
        Jan: "01",
        Feb: "02",
        Mar: "03",
        Apr: "04",
        May: "05",
        Jun: "06",
        Jul: "07",
        Aug: "08",
        Sep: "09",
        Oct: "10",
        Nov: "11",
        Dec: "12",
    };

    const [day, month, year] = date.split(" ");
    const formattedDay = day
        .split("")
        .filter((v) => !Number.isNaN(parseInt(v)))
        .join("");

    return `${year}-${months[month]}-${formattedDay.length >= 2 ? formattedDay : "0" + formattedDay
        }`;
}