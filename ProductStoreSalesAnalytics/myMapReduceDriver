import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

/*
 * 1) Instead of breaking the sales down by store, 
 * 			instead give us a sales breakdown by product category across all of our stores.
 * 
 * 2) Find the monetary value for the highest individual sale for each separate store.
 * 
 * 3) Find the total sales value across all the stores, and the total number of sales. 
 * 			Assume there is only one reducer.
 * 
 */
public class myMapReduceDriver extends Configured implements Tool {

	public static void main(String[] args) 
			throws Exception {
		// TODO Auto-generated method stub
		
		myMapReduceDriver driver = new myMapReduceDriver();
		
		System.exit(ToolRunner.run(driver, args));
	}

	public int run(String[] arg0) throws Exception {
		// TODO Auto-generated method stub
		if(arg0.length != 2) {
			System.err.println("Usage: Please supply Input file and output directory.");
			System.exit(1);
		}
		
		Job job = new Job();
		job.setJarByClass(myMapReduceDriver.class);
		job.setJobName("Sales per product category");
		
		job.setMapperClass(SalesPerStoreMapper.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(DoubleWritable.class);
		
		job.setReducerClass(TotalSalesValueAllStoresReducer.class);
		
		FileInputFormat.addInputPath(job, new Path(arg0[0]));
		FileOutputFormat.setOutputPath(job, new Path(arg0[1]));
		
		return job.waitForCompletion(true) ? 0:1;
	}

}
