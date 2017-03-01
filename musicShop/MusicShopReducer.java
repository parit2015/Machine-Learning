import java.io.IOException;
import java.util.HashSet;
import java.util.Set;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Reducer;

public class MusicShopReducer extends Reducer<IntWritable, IntWritable, IntWritable, IntWritable>{	
	
	@Override
	public void reduce(IntWritable trackId, Iterable<IntWritable> userIds, Context context)
			throws IOException, InterruptedException{
	
			System.out.println("In reducer class");
			Set<Integer> userIdSet = new HashSet<Integer>();
			
			for(IntWritable userId : userIds){
				userIdSet.add(userId.get());
				System.out.println(userIdSet.size());
			}
			
			IntWritable size = new IntWritable(userIdSet.size());
			context.write(trackId, size);
	}
}
