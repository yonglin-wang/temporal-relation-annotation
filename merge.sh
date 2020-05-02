output_path="./jonne-correct"

mkdir -p $output_path

for f in "./Jonne/*"
do
    for doc in $f #$(ls $f | grep xml)
    do
        for file in $doc/*.xml
        do
            ann_file=$(echo $file | sed s/Jonne/data/g)
            yflnyt_folder=$(echo $file | grep -Eo "YFLNYT_[0-9]*")
            xml_file=$(echo $file | grep -Eo 'P\_[0-9]*\.xml')
            full_output_path="${output_path}/${yflnyt_folder}"
            mkdir -p $full_output_path
            tohere="${full_output_path}/${xml_file}"
            echo "Populating ${file} using ${ann_file} and saving in ${tohere}"
            python merge-trees.py \
                --annotated-xml-path $ann_file \
                --unannotated-xml-path $file \
                --output-path $tohere
        done
    done
done



