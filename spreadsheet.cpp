#include <string>

std::string sort_csv_columns(const std::string& csv_data) {
    // raw string
    std::stringstream ss(csv_data);
    std::string to;
    std::vector<std::string> rows;
    if (&csv_data != NULL)
    {
        while (std::getline(ss, to, '\n')) {
            rows.push_back(to);
        }
    }

    std::stringstream firstline(rows[0]);
    std::map<std::string, int> keys;
    int index = 0;
    while (firstline.good())
    {
        std::string substr;
        getline(firstline, substr, ',');
        keys[substr] = index;
        index++;
    }

    //keys are the columns
    std::map<int, std::vector<std::string>> temp;
    for (int i = 0; i < keys.size(); i++) {
        temp[i] = std::vector<std::string>();
    }

    for (int i = 1; i < rows.size(); i++) {
        std::stringstream row(rows[i]);
        std::string substr;
        int index = 0;
        while (row.good())
        {
            getline(row, substr, ',');
            temp[index].push_back(substr);
            index++;
        }
    }

    std::map<std::string, std::vector<std::string>> newcsv;
    index = 0;
    for (std::map<string, int>::iterator i = keys.begin(); i != keys.end(); i++)
    {
        newcsv[i->first] = temp[i->second];
    }

    // build new string, with columns named sorted and rows in new line
    // keys are the columns headers
    // each column is separeted by a comma
    std::stringstream newcsv_string;
    // add first line of kyes to new string
    for (std::map<std::string, int>::iterator i = keys.begin(); i != keys.end(); i++)
    {
        newcsv_string << i->first << ",";
    }
    newcsv_string << "\n";
    // add the rest of the lines
    int rows_num = newcsv[keys.begin()->first].size();
    int columns_num = keys.size();

    for(int index = 0; index < rows_num; index++)
    {
        for (std::map<std::string, std::vector<std::string>>::iterator i = newcsv.begin(); i != newcsv.end(); i++)
        {
            newcsv_string << i->second[index] << ",";
        }
        // remove last comma
        newcsv_string.seekp(-1, std::ios_base::end);
        newcsv_string << "\n";
    }
   
    //remove last new line
    newcsv_string.seekp(-1, std::ios_base::end);
    result = newcsv_string.str();
    //remove new line from result
    result.erase(std::remove(result.begin(), result.end(), '\n'), result.end());
    return result;


}

 // raw string

std::string input = "Adam,Beth,Charles,Danielle,Eric\n
3907,17945,10091,10088,10132\n
48,2,12,13,11"