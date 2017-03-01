import java.io.IOException;
import java.text.DecimalFormat;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;


public class MaxSalesPerStoreReducer extends Reducer<Text, DoubleWritable, Text, Text>{

	@Override
	public void reduce(Text storeName, Iterable<DoubleWritable> salesPerStoreListByMapper, Context context)
			throws IOException, InterruptedException {
		
		Double maxSalesPerStore = 0.0;
		for (DoubleWritable salesIndividual : salesPerStoreListByMapper) {
			
			/*
			 * Finding out maximum sales value from the salesListFromMapper
			 */
			maxSalesPerStore = Math.max(maxSalesPerStore, salesIndividual.get());
		}
		
		/*
		 * Writing the context for storeName and MaxSales of same store
		 */
		context.write(storeName, new Text(new DecimalFormat("#.##").format(maxSalesPerStore)));
	}
}
