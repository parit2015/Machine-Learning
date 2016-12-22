import java.io.IOException;
import java.text.DecimalFormat;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;


public class TotalSalesPerProductReducer extends Reducer<Text, DoubleWritable, Text, Text> {
	
	@Override
	public void reduce(Text productName, Iterable<DoubleWritable> salesListFromMapper, Context context)
		throws IOException, InterruptedException {
		
		/*
		 * Calulating the total sales from the list of sales present with its corresponding productname
		 */
		Double totalSalesPerProduct = 0.0;	
		for (DoubleWritable salesToBeAdded : salesListFromMapper)
			totalSalesPerProduct += salesToBeAdded.get();
		
		/*
		 * Writing the context by 2 places precision to sales/product
		 */
		context.write(productName, new Text(new DecimalFormat("#.##").format(totalSalesPerProduct)));
	}
}
