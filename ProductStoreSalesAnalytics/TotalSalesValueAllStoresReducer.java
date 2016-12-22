import java.io.IOException;
import java.text.DecimalFormat;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;


public class TotalSalesValueAllStoresReducer extends Reducer<Text, DoubleWritable, Text, Text>{

	@Override
	public void reduce(Text storeName, Iterable<DoubleWritable> salesValueFromMapper, Context context)
			throws IOException, InterruptedException {
		
		Integer numOfSalesPerStore = new Integer(0);	
		Double totalSalesValuePerStore = new Double(0.0);
	
		/*
		 * Calculating numberOfSales and TotalSalesValues correspondingly, per store
		 */
		for (DoubleWritable individualSales : salesValueFromMapper) {
			
			totalSalesValuePerStore += individualSales.get();
			numOfSalesPerStore += 1;
		}
		
		/*
		 * Combined to show a single entry for NumberOfSales and TotalSalesValue
		 */
		String mergedValue = numOfSalesPerStore + " - " +  new DecimalFormat("#.##").format(totalSalesValuePerStore);
		
		/*
		 * Writing the context 
		 */
		context.write(storeName, new Text(mergedValue));		
	}
}
