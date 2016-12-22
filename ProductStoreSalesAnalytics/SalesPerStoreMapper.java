import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

/*
 * Maximum sales value in a store
 */
public class SalesPerStoreMapper extends Mapper<LongWritable, Text, Text, DoubleWritable>{

	Text storeName = new Text();
	DoubleWritable salesOfStore = new DoubleWritable();
	
	@Override
	public void map(LongWritable key, Text value, Context context)
		throws IOException, InterruptedException {
		
		String[] splittedPartsOfRecord = value.toString().split("\\t");
		
		/*
		 * Setting the storeName and corresponding sales per store
		 */
		storeName.set(splittedPartsOfRecord[StoreConstants.place]);
		salesOfStore.set(Double.parseDouble(splittedPartsOfRecord[StoreConstants.sales]));
		
		/*
		 * Writing the context for correct record, else incrementing the INVALID record count
		 */
		if(splittedPartsOfRecord.length == 6)
			context.write(storeName, salesOfStore);
		else
			context.getCounter(RecordCounter.INVALI_RECORD_COUNT).increment(1L);
	}
	
}
