import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

/*
 * Mapper to find out sales per product 
 * 
 * Sample Record:
 * 2012-01-01	09:00	San Jose	Men's Clothing	214.05	Amex
 * 
 * Product: Men's Clothing
 * Sales: 214.05
 */
public class SalesPerProductMapper extends Mapper<LongWritable, Text, Text, DoubleWritable>{
	
	Text productName = new Text();
	DoubleWritable salesOfProduct = new DoubleWritable();
	
	@Override
	public void map(LongWritable key, Text value, Context context)
		throws IOException, InterruptedException {
		
		String[] splittedPartsOfRecord = value.toString().split("\\t");
		
		/*
		 * Splitting and setting the key, value pair correspondingly
		 */
		productName.set(splittedPartsOfRecord[StoreConstants.product]);
		salesOfProduct.set(Double.parseDouble(splittedPartsOfRecord[StoreConstants.sales]));
		
		/*
		 * Adding the outcome of Product, Sales pair to context, so to pass to combiner
		 */
		if(splittedPartsOfRecord.length == 6)
			context.write(productName, salesOfProduct);
		
		/*
		 * In case of Illegal record, Increasing the Invalid record count
		 */
		else 
			context.getCounter(RecordCounter.INVALI_RECORD_COUNT).increment(1L);
		
	}
}